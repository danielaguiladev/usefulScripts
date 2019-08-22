param([String]$username = '')
Import-Module ActiveDirectory

function getUser($consoleParam) {
  Get-ADUser -f { $consoleParam -like $username } -Properties badPwdCount, department, homeDirectory, lastLogonTimeStamp, telephoneNumber, title, whenCreated, manager
}

if ($username -match '^\d+$') {
  getUser 'SamAccountName'
}
else {
  $username = $username + "*"
  getUser 'Name'
}