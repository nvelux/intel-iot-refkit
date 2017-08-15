import time
from oeqa.oetest import oeRuntimeTest


class PulseaudioTest(oeRuntimeTest):
    def test_rec_play(self):
        # Start pulseaudio daemon
        (status, output) = self.target.run("pulseaudio -D")
        self.assertEqual(status, 0, msg="Error pulseaudio not started: %s" % output)
        # Recording audio
        (status, output) = self.target.run("parecord -r /tmp/rec.wav &")
        time.sleep(10)
        self.assertEqual(status, 0, msg="Error not recorded: %s" % output)
        # Stop pulseaudio daemon
        (status, output) = self.target.run("killall -9 parecord")
        self.assertEqual(status, 0, msg="Error pulseaudio not stop: %s" % output)
        # start pulseaudio daemon
        time.sleep(10)
        (status, output) = self.target.run("pulseaudio -D")
        self.assertEqual(status, 0, msg="Error pulseaudio not started: %s" % output)
        # Checking recorded file present
        (status, output) = self.target.run("ls /tmp/ |grep 'rec.wav'")
        self.assertEqual(status, 0, msg="Error file not found: %s" % output)
        # Playing audio
        (status, output) = self.target.run("paplay /tmp/rec.wav &")
        self.assertEqual(status, 0, msg="Error not played: %s" % output)
        # state file copying
        (status, output) = self.target.run("pactl list sinks > /tmp/pula.txt")
        self.assertEqual(status, 0, msg="Error not copied: %s" % output)
        # Audio running states checking
        (status, output) = self.target.run("grep 'RUNNING' /tmp/pula.txt")
        self.assertEqual(status, 0, msg="Error not running: %s" % output)
