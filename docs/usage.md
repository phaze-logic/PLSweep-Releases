# Using PL Sweep

## Review before cleaning

1. Select the cleanup categories you want to inspect. Check browser and Recycle Bin selections before each run.
2. Set **Temp file age** (0–30 days) and the heavy-cleanup interval as needed.
3. Select **Preview Cleanup**.
4. Review each planned action, path, risk, reason, and estimated size. Clear **Clean** for items you want to keep.
5. Select **Proceed with Cleanup** and accept the confirmation only when the selected actions are appropriate.
6. Read the completion summary and Activity Log for warnings and incomplete actions.

Preview does not delete files, close browsers, empty the Recycle Bin, change registry entries, or run Windows maintenance commands. Size estimates can change before execution. **Ignore selected** saves paths to the ignore list; **Export preview** creates a CSV for review.

## Cleanup categories

| Category | What to review |
| --- | --- |
| Temporary files | User and Windows temporary files old enough to meet the age setting; empty temporary folders may also appear. |
| Browser cache | Supported Brave, Edge, Chrome, and Firefox locations for the current Windows user. Brave's standard option also targets browsing history. Chrome and Firefox standard cache options keep history, cookies, bookmarks, passwords, autofill, and extensions. |
| Browser privacy data | Additional session, site-storage, form-history, and privacy files. Review separately from cache cleanup. |
| All browser cookies | Explicit high-risk removal of cookie databases; may sign you out and remove site preferences. Saved passwords are not targeted. |
| Windows privacy traces | Recent Items, Jump Lists, thumbnail/icon caches, error/crash reports, and Windows Update download files. |
| Application caches | Supported cache/log locations for applications such as Discord, Teams, Steam, Adobe, and Office. |
| Broken shortcuts and empty folders | Missing-target shortcuts and empty folders in the supported scan locations. |
| Old Downloads | Personal files listed for review and left unselected by default. |

Optional categories must be selected to appear in the preview. A candidate is a reason to inspect an item, not proof that you no longer need it.

The expanded **browser privacy** and **all browser cookies** scans inspect all
supported browsers they detect, independently of the standard browser cache
checkboxes. Selecting **Include all browser cookies** also includes the broader
privacy targets, which can include history, sessions, Local Storage, and
IndexedDB. Review that combined preview and clear **Clean** for any browser or
data category you want to retain; selecting cookies is not a cookies-only scan.

## Browser behavior

**Do not close browsers** skips browser cleanup even when the browser is already closed. To clean browser data, disable that option, save your browser work, and close the browser yourself before generating a new preview.

With browser cleanup enabled, PL Sweep attempts to close browser processes and may force-close remaining background processes. Do not rely on a running browser profile being automatically skipped: approved path operations can still be attempted if processes remain. Locked files may fail, and the Activity Log records warnings. Avoid reopening a browser until cleanup finishes.

## Recovery and permanent operations

Quarantine is enabled by default for approved file cleanup. Successfully moved items are stored under `%LOCALAPPDATA%\PL Sweep\Quarantine`; Settings can open that folder or restore the latest session. Retention defaults to 14 days and is configurable from 1–90 days. Expired sessions can be permanently removed during later cleanup. Quarantine keeps the file data on disk, so moving files there does not immediately reclaim their storage.

Restore skips an item if its original path already exists. Review the restore result; quarantine is not a complete backup or a guarantee that every change can be undone.

| Action | Recovery boundary |
| --- | --- |
| File cleanup with quarantine enabled | Successfully moved files may be restored while the session remains available. |
| File cleanup with quarantine disabled | Files are deleted directly; PL Sweep provides no undo. |
| **Empty Recycle Bin** | Permanently removes current bin contents; no quarantine or app undo. |
| **Purge Selected** in Scan Leftovers | Permanently deletes selected folders; no quarantine or app undo. |
| Heavy cleanup | Delivery Optimization cleanup and DISM component maintenance are Windows operations, outside file quarantine. |
| Registry cleaning/restoration | Uses registry exports, not file quarantine; changes can affect applications and Windows behavior. |

Heavy cleanup normally runs when its configured interval is due (default: 7 days). **Force heavy cleanup today** bypasses that interval. DISM can take several minutes and may need administrator permission. It runs component-store cleanup, not a quarantined file deletion.

## Leftover and registry scans

**Scan Leftovers** reviews likely application/profile leftovers and creates a CSV. Inspect each folder before **Purge Selected**; unfamiliar names alone do not justify deletion.

**Scan Registry** reviews possible stale uninstall, startup, service, and App Paths references and creates a CSV. A missing referenced path can have legitimate explanations. **Clean Selected** requires a fresh registry backup and another confirmation. Cleaning may remove values, keys, or stale service entries; machine-wide changes may require elevation.

**Backup Registry** exports current-user and local-machine hives. **Restore Registry** accepts a complete app-created backup from its backup location. Restoring imports backed-up values and can overwrite current registry data; it is not a precise undo of just the selected cleanup entries. Save work and review the backup before restoring.

## Settings and reports

Settings include cleanup defaults, reports, registry safety, theme, and accessibility options. Default user data is under `%LOCALAPPDATA%\PL Sweep`; report and registry-backup locations can be configured. Treat reports and backups as sensitive. See [Privacy](privacy.md).

`PLSweep.exe --autorun` opens the app and starts a preview; it does not approve or execute cleanup.

See [Troubleshooting](troubleshooting.md), [Support](../SUPPORT.md), or the [documentation index](README.md).
