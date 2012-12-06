<#list features as feature>
    {
    <#list feature.attributes as attribute>
        <#if !attribute.isGeometry>
            "${attribute.name}": "${attribute.value}",
        </#if>
    </#list>
            "tmp": "tmp"
    },
</#list>
{"tmp": "tmp"}
