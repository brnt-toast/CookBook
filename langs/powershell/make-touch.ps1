reate an alias 'touch' for 'New-Item -Type File'
Set-Alias -Name touch -Value "New-Item" -Option AllScope

# Create a function to wrap the behavior of `touch` for creating files
# function touch {
#     param(
#             [string]$Path
#                 )
#                     # Use New-Item to create the file if it doesn't exist, otherwise update its last write time
#                         if (-Not (Test-Path -Path $Path)) {
#                                 New-Item -Path $Path -ItemType File -Force
#                                     } else {
#                                             (Get-Item -Path $Path).LastWriteTime = Get-Date
#                                                 }
#                                                 }
#
