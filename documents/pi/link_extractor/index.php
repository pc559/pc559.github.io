<html><body><h1>Links, from Facebook groups.</h1>
<title>WoOooOOOoooooOOOOOOOO</title>

<p>Gimme access token</p>
<form method="post">
<input type="text" name="token" maxlength="500"/>
</form>

<p>Gimme group num</p>
<form method="post">
<input type="text" name="num" maxlength="100">
</form>


<?php
$token = $_POST["token"];
$group = $_POST["num"];

if($token!="")
{
$t = fopen("scraper/token.txt",'w');

fwrite($t,$token);
fclose($t);
}

if($group!="")
{
$g = fopen("scraper/group.txt",'w');

fwrite($g,$group);
fclose($g);
}

//echo exec('./scraper/group_scraper.py');
//command = escapeshellcmd('./scraper/group_scraper.py');
//system(command);

?>

<br>
<button onclick="exec('./scraper/group_scraper.py')">Someday this will actually do something</button>
<br>

</body></html>

