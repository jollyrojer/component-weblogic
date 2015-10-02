Oracle WebLogic Server
=====

Version 1.1-35p
-------------

![](http://www.oracle.com/ocom/groups/public/@otn/documents/digitalasset/352606.gif)

Installs and configures Oracle Weblogic Server

[![Install](https://raw.github.com/qubell-bazaar/component-skeleton/master/img/install.png)](https://express.tonomi.com/applications/upload?metadataUrl=https://raw.github.com/qubell-bazaar/component-oracle-weblogic/1.1-35p/meta.yml)

Features
--------

 - Install and configure Oracle WebLogic Server
   - 11g (version 10.3.6)
   - 12g (version 12.1.2)

Pre-requisites
--------------

 - AWS account
 - Centos 6 x86_64 ([AWS Marketplace](https://aws.amazon.com/marketplace/pp/B00A6KUVBW))
 - Oracle WebLogic Server distribution: [Download](http://www.oracle.com/technetwork/middleware/weblogic/downloads/wls-main-097127.html)

Configuration
-------------

 - Launch/configure Cloud Account in desired region:
   - N.California (us-west-1)
   - Oregon (us-west-2)
   - N.Virginia (us-east-1)
 - Create enviroment property `oracle_weblogic_install` with type `map<string, object>` and contents:
```
jar: "http://url.to/wls1036.jar"
```
