from lxml import etree

# Load XML
xml_tree = etree.parse("file:///C:/Users/91918/Videos/Captures/dtdexample/Product.xml")

# Load XSL
xsl_transform = etree.XSLT(etree.parse("file:///C:/Users/91918/Videos/Captures/dtdexample/productxsl.xsl"))

# Apply XSLT transformation
html_tree = xsl_transform(xml_tree)


# Write transformed HTML to a file
with open("Productoutput.html", "wb") as output_file:
    output_file.write(etree.tostring(html_tree, pretty_print=True))