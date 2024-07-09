import glob
import os
import subprocess

from StaticLifterRunner import StaticLifterRunner

class LeanbinLifterRunner(StaticLifterRunner):
    def __init__(self, lifter):
        super().__init__(lifter)

    def get_name(self):
        return "Lifter (LeanBin)"

    def recompile(self, binary):
        subprocess.run(["sh"] + [os.path.join(os.path.dirname(self.lifter), "bash/generate-source.sh")] + [binary], capture_output=True, cwd=os.path.dirname(binary), check=True)
        if "Xalan" in binary:
            subprocess.run(["bash"] + [os.path.join(os.path.dirname(self.lifter), "bash/patch-and-compile.sh")] + ["--no-inline", binary], capture_output=True, cwd=os.path.dirname(binary), check=True)
            subprocess.run(["bash"] + [os.path.join(os.path.dirname(self.lifter), "bash/patch-and-compile.sh")] + ["--out", binary + "_lifted_size", "--size-no-inline", binary], capture_output=True, cwd=os.path.dirname(binary), check=True)
            subprocess.run(["bash"] + [os.path.join(os.path.dirname(self.lifter), "bash/patch-and-compile.sh")] + ["--out", binary + "_lifted_pac", "--pac-no-inline", binary], capture_output=True, cwd=os.path.dirname(binary), check=True)
        else:
            subprocess.run(["bash"] + [os.path.join(os.path.dirname(self.lifter), "bash/patch-and-compile.sh")] + [binary], capture_output=True, cwd=os.path.dirname(binary), check=True)
            subprocess.run(["bash"] + [os.path.join(os.path.dirname(self.lifter), "bash/patch-and-compile.sh")] + ["--out", binary + "_lifted_size", "--size", binary], capture_output=True, cwd=os.path.dirname(binary), check=True)
            subprocess.run(["bash"] + [os.path.join(os.path.dirname(self.lifter), "bash/patch-and-compile.sh")] + ["--out", binary + "_lifted_pac", "--pac", binary], capture_output=True, cwd=os.path.dirname(binary), check=True)

    def cleanup(self, binary):
        for f in glob.glob(os.path.join(os.path.dirname(binary), "*.mtrace")):
            os.remove(f)

        os.remove(binary + "_concat.c")
        os.remove(binary + "_lifted")
        os.remove(binary + "_lifted_size")
        os.remove(binary + "_lifted_pac")
        os.remove(os.path.join(os.path.dirname(binary), "blocks.txt"))
        os.remove(os.path.join(os.path.dirname(binary), "trampolines.S"))
        os.remove(os.path.join(os.path.dirname(binary), "custom.ld.part2"))
