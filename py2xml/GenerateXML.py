from lxml import etree
import os

class GenerateXML(object):
    def generate_xml(self, modules_path, xmlfile, xslfile = None, recursive = False):
        self.modules_node = etree.Element("modules")
        if os.path.isdir(modules_path):
            pyfiles = self._list_allpy(modules_path, recursive)
            for pyfile in pyfiles:
                self._append_librarynode(pyfile)
        elif os.path.isfile(modules_path):
            self._append_librarynode(modules_path)
        else:
            raise Exception("Modules path not exists")
        if xslfile != None:
            xsl_doctype = "<?xml-stylesheet href='modules.xsl' type='text/xsl'?>"
        modules_tree = etree.ElementTree(self.modules_node)
        modules_tree.write(xmlfile, pretty_print = True, xml_declaration = True, doctype = xsl_doctype, encoding = "utf-8")

    def _append_librarynode(self, pyfile):
        fp_pyfile = open(pyfile)

        library_node = etree.SubElement(self.modules_node, "library")
        library_node.set("path", pyfile)

        class_name = os.path.basename(pyfile).split(".")[0]
        if self._find_class(fp_pyfile, class_name) != True:
            return False
        class_node = etree.SubElement(library_node, "class")
        class_node.set("name", os.path.basename(pyfile).split(".")[0])
        recent_node = class_node

        line = fp_pyfile.readline()
        while (line):
            line_lstrip = line.lstrip()
            if line_lstrip.startswith("class "):
                break
            elif line_lstrip.startswith("__name__"):
                break
            elif line_lstrip.startswith("def _"):
                return_flag = 0
            elif line_lstrip.startswith("def "):
                return_flag = 1
                def_node = etree.SubElement(class_node, "def")
                defname = self._get_defname(fp_pyfile, line_lstrip)
                def_node.set("name", defname)
                recent_node = def_node
            elif line_lstrip.startswith("return "):
                if return_flag == 1:
                    return_value = line_lstrip.replace("return", "").lstrip().rstrip()
                    exist_flag = 0
                    for exist_return_value in recent_node.itertext("return"):
                        if return_value == exist_return_value:
                            exist_flag = 1
                            break
                    if exist_flag == 0:
                        return_node = etree.SubElement(recent_node, "return")
                        return_node.text = return_value
            elif line_lstrip.startswith("\"\"\""):
                comment_node = etree.SubElement(recent_node, "comment")
                comment_node.text = etree.CDATA(self._get_comment_text(fp_pyfile, line_lstrip, "\"\"\""))
            elif line_lstrip.startswith("'''"):
                comment_node = etree.SubElement(recent_node, "comment")
                comment_node.text = etree.CDATA(self._get_comment_text(fp_pyfile, line_lstrip, "'''"))

            line = fp_pyfile.readline()

        fp_pyfile.close()

    def _get_comment_text(self, fp_pyfile, current_lstrip_line, comment_head):
        if current_lstrip_line.lstrip("'").rstrip().endswith(comment_head):
            comment_text = current_lstrip_line.lstrip(comment_head[0]).rstrip().rstrip(comment_head[0])
        else:
            firstline_flag = 1
            comment_text = current_lstrip_line.lstrip(comment_head[0]).rstrip()
            line = fp_pyfile.readline()
            while (line):
                line_lstrip = line.lstrip()
                if line_lstrip.startswith(comment_head) != True:
                    if firstline_flag == 0:
                        comment_text += "<br />"
                    else:
                        firstline_flag = 0
                    if line_lstrip.rstrip().endswith(comment_head) != True:
                        comment_text += line_lstrip.rstrip()
                    else:
                        comment_text += line_lstrip.rstrip().rstrip(comment_head[0])
                        break
                else:
                    break
                line = fp_pyfile.readline()

        return comment_text

    def _get_defname(self, fp_pyfile, current_lstrip_line):
        if current_lstrip_line.rstrip().endswith("):"):
            defname = current_lstrip_line.replace("def ", "").replace("self, ", "").rstrip().rstrip(":")
        else:
            defname = current_lstrip_line.replace("def ", "").replace("self, ", "").rstrip()
            line = fp_pyfile.readline()
            while (line):
                if line.rstrip.endswith("):") != True:
                    defname += line.lstrip().rstrip()
                else:
                    defname += line.lstrip().split("):")[0]
                    break
                line = fp_pyfile.readline()

        return defname

    def _find_class(self, fp_pyfile, class_name):
        line = fp_pyfile.readline()
        pre_classname = "class " + class_name
        while (line):
            if line.lstrip().startswith(pre_classname):
                return True
            line = fp_pyfile.readline()

        return False

    def _list_allpy(self, path, recursive):
        pyfiles = []
        file_all_paths = []
        if recursive == True:
            for dirpath, dirnames, filenames in os.walk(path):
                for filename in filenames:
                    file_all_paths.append(os.path.join(dirpath, filename))
        else:
            filenames = os.listdir(path)
            for filename in filenames:
                file_all_paths.append(os.path.join(path, filename))

        for file_all_path in file_all_paths:
            if self._is_pyfile(file_all_path):
                pyfiles.append(file_all_path)

        return pyfiles

    def _is_pyfile(self, filename):
        file_basename = os.path.basename(filename)

        if file_basename.endswith(".py") and \
                file_basename[0] != "_" and \
                file_basename[0].isupper() == True:
            return True
        else:
            return False

if __name__ == "__main__":
    CL = GenerateXML()
    CL.generate_xml("modules", "modules.xml", "modules.xsl")
