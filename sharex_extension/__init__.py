from fman import DirectoryPaneCommand, show_alert
from fman.url import as_human_readable
import subprocess

class ShareX(DirectoryPaneCommand):
	def __call__(self):
		exe_path = "C:\\Program Files\\ShareX\\ShareX.exe"
		paths = self.pane.get_selected_files()
		# if paths length != 1 return
		if len(paths) != 1:
			show_alert("You can only share exactly one file at a time")
			return
		subprocess.call(f'"{exe_path}"  "{as_human_readable(paths[0])}"')