$exclude = @("venv", "botmebuki.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "botmebuki.zip" -Force