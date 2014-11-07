<map version="0.9.0">
<!-- To view this file, download free mind mapping software FreeMind from http://freemind.sourceforge.net -->
<node CREATED="1413219609539" ID="ID_1567602614" MODIFIED="1415380857448" TEXT="Modelo">
<node CREATED="1413219625350" ID="ID_720884399" MODIFIED="1413219626058" POSITION="right" TEXT="Status">
<node CREATED="1413219638581" ID="ID_393474756" MODIFIED="1413220140455" TEXT="name">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      Pode ser um dos subitens deste n&#243;
    </p>
  </body>
</html></richcontent>
<node CREATED="1413219647629" ID="ID_1845174396" MODIFIED="1415380860542" TEXT="created">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      Status padr&#227;o. Nesse momento o projeto foi apenas criado e seus dados informados.
    </p>
  </body>
</html></richcontent>
<node CREATED="1413220734069" ID="ID_338875003" MODIFIED="1413220739577" TEXT="Status padr&#xe3;o"/>
</node>
<node CREATED="1413219651797" ID="ID_1286935041" MODIFIED="1415380860543" TEXT="structured">
<node CREATED="1412281583648" ID="ID_316071032" MODIFIED="1412281602596" TEXT="Canal de comunica&#xe7;&#xe3;o deve existir"/>
<node CREATED="1412280012849" ID="ID_1953864908" MODIFIED="1412280055622" TEXT="Reposit&#xf3;rio do projeto deve existir"/>
<node CREATED="1412280071753" ID="ID_268092569" MODIFIED="1412281957651" TEXT="Estrutura do WP deve existir no reposit&#xf3;rio"/>
</node>
<node CREATED="1413219656069" ID="ID_643500948" MODIFIED="1415380860545" TEXT="development">
<node CREATED="1412280111112" ID="ID_438261912" MODIFIED="1412281759312" TEXT="Server de testing deve existir"/>
<node CREATED="1412280156016" ID="ID_727116439" MODIFIED="1412280168061" TEXT="Server de testing deve possuir uma c&#xf3;pia do projeto"/>
<node CREATED="1412281790623" ID="ID_211351322" MODIFIED="1412281804676" TEXT="Server de testing deve possuir um webserver rodando"/>
</node>
<node CREATED="1413219658765" ID="ID_1421806857" MODIFIED="1415380860547" TEXT="staging">
<node CREATED="1412280127208" ID="ID_1331305189" MODIFIED="1412280135005" TEXT="Servidor de produ&#xe7;&#xe3;o deve existir"/>
<node CREATED="1412280156016" ID="ID_18129804" MODIFIED="1412280296228" TEXT="Server de produ&#xe7;&#xe3;o deve possuir uma c&#xf3;pia do projeto"/>
<node CREATED="1412281868175" ID="ID_509454931" MODIFIED="1412281873572" TEXT="Server de produ&#xe7;&#xe3;o deve possuir um webserver rodando"/>
</node>
<node CREATED="1413219660941" ID="ID_1982307896" MODIFIED="1415380860547" TEXT="maturation">
<node CREATED="1412280324175" ID="ID_1842178316" MODIFIED="1412280338772" TEXT="Deploy deve ter sido conclu&#xed;do ao menus uma vez com sucesso"/>
</node>
<node CREATED="1413219663725" ID="ID_1911706368" MODIFIED="1415380860548" TEXT="maintenance">
<node CREATED="1412280350103" ID="ID_876591005" MODIFIED="1412280548891" TEXT="Data atual deve estar dentro do per&#xed;odo de manuten&#xe7;&#xe3;o"/>
</node>
<node CREATED="1413219666581" ID="ID_1578562353" MODIFIED="1415380860549" TEXT="delivered">
<node CREATED="1412280350103" ID="ID_1146022333" MODIFIED="1412280566131" TEXT="Data atual deve estar depois do per&#xed;odo de manuten&#xe7;&#xe3;o"/>
</node>
</node>
</node>
<node CREATED="1413220824724" ID="ID_782675930" MODIFIED="1413220911096" POSITION="right" TEXT="Person">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      Depois deixar mais male&#225;vel, dever&#225; poder inserir quaisquer contatos que a pessoa possua
    </p>
  </body>
</html></richcontent>
<node CREATED="1413220847836" ID="ID_910499999" MODIFIED="1413220850769" TEXT="name"/>
<node CREATED="1413220850988" ID="ID_590052249" MODIFIED="1413220854569" TEXT="email"/>
<node CREATED="1413220855236" ID="ID_1251660285" MODIFIED="1413220856881" TEXT="skype"/>
<node CREATED="1413220845940" ID="ID_21578350" MODIFIED="1413220880088" TEXT="person -&gt; AUTH_USER_MODEL (do django)">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      Toda pessoa deve estar associada a um usu&#225;rio do django
    </p>
  </body>
</html></richcontent>
</node>
</node>
<node CREATED="1413219989603" ID="ID_397339849" MODIFIED="1413221144602" POSITION="right" TEXT="ProjectPerson">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      Tabela de relacionamento N x N entre Person e Project
    </p>
  </body>
</html></richcontent>
<node CREATED="1413220999755" ID="ID_949781045" MODIFIED="1413221151182" TEXT="person -&gt; Person"/>
<node CREATED="1413220042090" ID="ID_1362349948" MODIFIED="1413220045287" TEXT="role">
<node CREATED="1413220046658" ID="ID_336450827" MODIFIED="1413221219220" TEXT="team_leader">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      S&#243; dever&#225; existir um por projeto
    </p>
  </body>
</html></richcontent>
</node>
<node CREATED="1413220052914" ID="ID_1505180956" MODIFIED="1413221077020" TEXT="developper"/>
<node CREATED="1413220049602" ID="ID_742299015" MODIFIED="1413221080302" TEXT="customer_leader"/>
<node CREATED="1413221080882" ID="ID_1084043458" MODIFIED="1413221108222" TEXT="customer_participant"/>
</node>
<node CREATED="1413219995227" ID="ID_200754722" MODIFIED="1413221152916" TEXT="project -&gt; Project"/>
</node>
<node CREATED="1413219684597" ID="ID_478338140" MODIFIED="1413219687370" POSITION="right" TEXT="Project">
<node CREATED="1413219695421" ID="ID_1525805288" MODIFIED="1413219698274" TEXT="name"/>
<node CREATED="1413219698501" ID="ID_101555925" MODIFIED="1413219699569" TEXT="slug"/>
<node CREATED="1413219699773" ID="ID_386786078" MODIFIED="1413219703761" TEXT="customer_name"/>
<node CREATED="1413219705813" ID="ID_611429153" MODIFIED="1413221246806" TEXT="current_status -&gt; Status"/>
<node CREATED="1413219769380" ID="ID_818400408" MODIFIED="1413221470044" TEXT="is_model">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      Tipo booleano. Se =True indica que o projeto &#233; na verdade um template de projeto, isto &#233;, n&#227;o deve ser exibido nas listagens de projeto.
    </p>
  </body>
</html></richcontent>
</node>
</node>
<node CREATED="1413219777492" ID="ID_609489724" MODIFIED="1413221570089" POSITION="right" TEXT="ExternalCommand">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      Classe gen&#233;rica para comandos ao balc&#227;o que ser&#227;o executados dinamicamente.
    </p>
  </body>
</html></richcontent>
<node CREATED="1413219787988" ID="ID_1952028613" MODIFIED="1413219789489" TEXT="name"/>
<node CREATED="1413219789700" ID="ID_1150914504" MODIFIED="1413219797629" TEXT="python_command_line"/>
<node CREATED="1413219799020" ID="ID_385491490" MODIFIED="1413219803401" TEXT="status -&gt; Status"/>
</node>
<node CREATED="1413219939299" ID="ID_18333942" MODIFIED="1413221604927" POSITION="right" TEXT="Sensor (extends ExternalCommand)">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      &#201; um comando externo que devolve dados ao balc&#227;o. Sua principal fun&#231;&#227;o &#233; fazer monitoramento de recursos.
    </p>
  </body>
</html></richcontent>
<node CREATED="1413221684541" ID="ID_1808928136" MODIFIED="1413221697754" TEXT="data">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      Dados retornados pelo sensor
    </p>
  </body>
</html></richcontent>
</node>
</node>
<node CREATED="1413219941907" ID="ID_529453277" MODIFIED="1413221675222" POSITION="right" TEXT="Action (extends ExternalCommand)">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      Comando externo que tem por finalidade executar uma a&#231;&#227;o apenas, seu &#250;nico valor de retorno &#233; ok/failed
    </p>
  </body>
</html></richcontent>
<node CREATED="1413221676838" ID="ID_1991360651" MODIFIED="1413221714341" TEXT="status">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      Status indicando ok/falha ao executar o comando
    </p>
  </body>
</html></richcontent>
</node>
</node>
</node>
</map>
