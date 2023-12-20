```
<portType name="DateServicePortType">
  <operation name="getDate">
    <input message="tns:getDateRequestMessage"/>
    <output message="tns:getDateResponseMessage"/>
  </operation>
  <operation name="getWeekday">
    <input message="tns:getWeekdayRequestMessage"/>
    <output message="tns:getWeekdayResponseMessage"/>
  </operation>
  <operation name="getMonth">
    <input message="tns:getMonthRequestMessage"/>
    <output message="tns:getMonthResponseMessage"/>
  </operation>
  <operation name="getYear">
    <input message="tns:getYearRequestMessage"/>
    <output message="tns:getYearResponseMessage"/>
  </operation>
</portType>

```
