Script to automatically refactor "han" with a site name.

1. change the directory name and the file name

   - features/org.csstudio.han.product.configuration.feature/
   - repository/cs-studio-han.product


find  -type d -name '*template*' | head -n1
./features/org.csstudio.template.product.configuration.feature


find  -type f -name '*template*' | head -n1
./repository/cs-studio-template.product


grep --exclude={*.py,*.md} -rl "template" *



jhlee@kaffee:~/org.csstudio.template.product (refactor)$ grep --exclude={*.py,*.md,*.target,*.sh} -inr "template" *

features/org.csstudio.template.product.configuration.feature/feature.xml:3:      id="org.csstudio.template.product.configuration.feature"
features/org.csstudio.template.product.configuration.feature/.project:3:        <name>org.csstudio.template.product.configuration.feature</name>
features/org.csstudio.template.product.configuration.feature/pom.xml:10:  <artifactId>org.csstudio.template.product.configuration.feature</artifactId>
features/pom.xml:5:    <artifactId>template-product</artifactId>
features/pom.xml:12:          org.csstudio.template.product.configuration.feature
pom.xml:5:    <artifactId>template-product</artifactId>
pom.xml:8:    <name>Template CS-Studio Product</name>
pom.xml:9:    <description>An Template for creating your own CS-Studio product</description>
pom.xml:32:     <product.name>cs-studio-template</product.name>
repository/cs-studio-template.product:4:<product name="Cs-studio-template" uid="cs-studio-template" id="org.csstudio.product.product" application="org.csstudio.product.application" version="4.2.0" useFeatures="true" includeLaunchers="true">
repository/cs-studio-template.product:47:         <ico path="/template-product/repository/icons/css.ico"/>
repository/cs-studio-template.product:75:      <feature id="org.csstudio.template.product.configuration.feature"/>
repository/pom.xml:6:        <artifactId>template-product</artifactId>



grep --exclude={*.py,*.md,*.target,*.sh} -rl "template" * | xargs sed -i 's/[Tt]emplate/han/g'
