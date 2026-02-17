@echo off
:: Define paths (Quote them if they have spaces)
set "SOURCE=C:\Users\Alessandro\Documents\Obsidian\Alex's Second Brain"
set "DEST=C:\Users\Alessandro\quartz_kb\content"

:: /MIR  :: Mirror directory tree (Equivalent to rsync --delete)
:: /XD   :: Exclude Directories (Prevent syncing .git or private folders)
:: /XF   :: Exclude Files (Optional)
:: /R:0  :: 0 Retries on failed copies
:: /W:0  :: 0 Wait time between retries

robocopy "%SOURCE%" "%DEST%" /MIR /XD ".git" ".obsidian" "Private" /R:0 /W:0

echo Sync Complete.
pause