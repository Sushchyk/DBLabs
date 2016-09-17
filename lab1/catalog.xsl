<?xml version="1.0" encoding="UTF-8"?>

<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
  <html>
  <body>
  <h2>Catalog</h2>
  <table border="1">
    <tr bgcolor="#9acd32">
        <th>Title</th>
        <th>Description</th>
        <th>Image</th>
        <th>Price </th>
    </tr>
    <xsl:for-each select="data/product">
    <tr>
        <td><xsl:value-of select="title"/></td>
        <td><xsl:value-of select="description"/></td>
        <td>
            <img>
                <xsl:attribute name="src">
                    <xsl:value-of select="image"/>
                </xsl:attribute>
            </img>
        </td>
        <td><xsl:value-of select="price"/></td>
    </tr>
    </xsl:for-each>
  </table>
  </body>
  </html>
</xsl:template>

</xsl:stylesheet>