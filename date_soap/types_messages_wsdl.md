```
<types>
    <xsd:schema targetNamespace="http://example.com/date.wsdl">
      <xsd:element name="getDateRequest" type="xsd:string"/>
      <xsd:element name="getDateResponse" type="xsd:string"/>
    </xsd:schema>
</types>

<message name="getDateRequestMessage">
    <part name="parameters" element="tns:getDateRequest"/>
</message>

<message name="getDateResponseMessage">
    <part name="parameters" element="tns:getDateResponse"/>
</message>
```
