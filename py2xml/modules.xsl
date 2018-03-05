<?xml version="1.0" encoding="utf-8"?>

<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:output method="html"/>
<xsl:template match="/modules">
  <html>
    <head>
      <title>Modules</title>
      <style type="text/css">
        #content {width:95%;}
        .zebra td, .zebra th {
          padding: 10px;
          border-bottom: 1px solid #f2f2f2;
        }

        .zebra tbody tr:nth-child(even) {
          background: #f5f5f5;
          -webkit-box-shadow: 0 1px 0 rgba(255,255,255,.8) inset;
          -moz-box-shadow:0 1px 0 rgba(255,255,255,.8) inset;
          box-shadow: 0 1px 0 rgba(255,255,255,.8) inset;
        }

        .zebra th {
          text-align: left;
          text-shadow: 0 1px 0 rgba(255,255,255,.5);
          border-bottom: 1px solid #ccc;
          background-color: #eee;
          background-image: -webkit-gradient(linear, left top, left bottom, from(#f5f5f5), to(#eee));
          background-image: -webkit-linear-gradient(top, #f5f5f5, #eee);
          background-image:    -moz-linear-gradient(top, #f5f5f5, #eee);
          background-image:     -ms-linear-gradient(top, #f5f5f5, #eee);
          background-image:      -o-linear-gradient(top, #f5f5f5, #eee);
          background-image:         linear-gradient(top, #f5f5f5, #eee);
        }

        .zebra th:first-child {
          -moz-border-radius: 6px 0 0 0;
          -webkit-border-radius: 6px 0 0 0;
          border-radius: 6px 0 0 0;
        }

        .zebra th:last-child {
          -moz-border-radius: 0 6px 0 0;
          -webkit-border-radius: 0 6px 0 0;
          border-radius: 0 6px 0 0;
        }

        .zebra th:only-child{
          -moz-border-radius: 6px 6px 0 0;
          -webkit-border-radius: 6px 6px 0 0;
          border-radius: 6px 6px 0 0;
        }

        .zebra tfoot td {
          border-bottom: 0;
          border-top: 1px solid #fff;
          background-color: #f1f1f1;
        }

        .zebra tfoot td:first-child {
          -moz-border-radius: 0 0 0 6px;
          -webkit-border-radius: 0 0 0 6px;
          border-radius: 0 0 0 6px;
        }

        .zebra tfoot td:last-child {
          -moz-border-radius: 0 0 6px 0;
          -webkit-border-radius: 0 0 6px 0;
          border-radius: 0 0 6px 0;
        }

        .zebra tfoot td:only-child{
          -moz-border-radius: 0 0 6px 6px;
          -webkit-border-radius: 0 0 6px 6px;
          border-radius: 0 0 6px 6px
        }
      </style>
    </head>
    <body>
      <h1>Modules</h1>
      <xsl:for-each select="library">
        <h2><xsl:value-of select="position()"/>. <xsl:value-of select="@path"/></h2>
        <xsl:for-each select="class">
          <h3><xsl:value-of select="@name"/></h3>
          <xsl:for-each select="comment">
            <xsl:value-of select="." disable-output-escaping="yes"/>
          </xsl:for-each>
          <xsl:if test="comment">
            <br/>
            <br/>
          </xsl:if>
          <div id="content">
            <table class="zebra">
              <tr>
                <th>Definition</th>
                <th>Description</th>
                <th>ReturnValue</th>
              </tr>
              <xsl:for-each select="def">
                <tr>
                  <td><xsl:value-of select="@name"/></td>
                  <td>
                    <xsl:for-each select="comment">
                        <xsl:value-of select="."/>
                    </xsl:for-each>
                  </td>
                  <td>
                    <xsl:for-each select="return">
                      <xsl:value-of select="."/>
                      <xsl:if test="position()!=last()">
                        <br/>
                      </xsl:if>
                    </xsl:for-each>
                  </td>
                </tr>
              </xsl:for-each>
            </table>
          </div>
        </xsl:for-each>
      </xsl:for-each>
    </body>
  </html>
</xsl:template>

</xsl:stylesheet>