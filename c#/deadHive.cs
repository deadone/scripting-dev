public class RegistryHive
{
    public RegistryHive(string file)
    {
        if (!File.Exists(file))
            throw new FileNoteFoundException();

        this.Filepath = file;

        using (FileStream stream = File.OpenRead(file))
        {
            using (BinaryReader reader = new BinaryReader(stream))
            {
                byte[] buf = reader.ReadBytes(4);

                if (buf[0] != 'r' || buf[1] != 'e' || buf[2] != 'g' || buf[3] != 'f')
                    throw new NotSuppportedException("File not a registry hive.");

                reader.BaseStream.Position = 4096 + 32 + 4;

                this.RootKey = new NodeKey(reader);
            }
        }
    }
    public string Filepath { get; set; }
    public NodeKey RootKey { get; set; }
    public bool WasExported { get; set; }
}
