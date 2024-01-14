<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="html" indent="yes"/>

    <xsl:template match="/">
        <html>
            <head>
                <title>Contact Information</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        display: flex;
                        flex-direction: column;
                        align-items: center;
                        justify-content: flex-start;
                        height: 100vh;
                        margin: 0;
                    }

                    h2 {
                        color: #3366cc;
                        font-size: 40px;
                    }

                    ul {
                        list-style-type: none;
                        padding: 5px;
                    }

                    li {
                        margin-bottom: 15px;
                        color: #1F4895;
                        font-size: 20px;
                    }
                </style>
            </head>
            <body>
                <h2>Contact Information</h2>
                <ul>
                    <li><strong>Owner: </strong> <xsl:value-of select="company/owner"/></li>
                    <li><strong>Email: </strong> <xsl:value-of select="company/email"/></li>
                    <li><strong>Address: </strong> <xsl:value-of select="company/address"/></li>
                    <li><strong>Phone: </strong> <xsl:value-of select="company/phone"/></li>
                </ul>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>