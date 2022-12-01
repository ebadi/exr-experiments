#### openexr

```
pip3 install openexr
Collecting openexr
  Downloading OpenEXR-1.3.9.tar.gz (13 kB)
Building wheels for collected packages: openexr
  Building wheel for openexr (setup.py) ... error
  ERROR: Command errored out with exit status 1:
   command: 'C:\Users\ITDforskning\Anaconda3\envs\Hamid\python.exe' -u -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'C:\\Users\\ITDforskning\\AppData\\Local\\Temp\\pip-install-47_87ann\\openexr_3db9b944eb864b58bbf232dc3e4ea1b4\\setup.py'"'"'; __file__='"'"'C:\\Users\\ITDforskning\\AppData\\Local\\Temp\\pip-install-47_87ann\\openexr_3db9b944eb864b58bbf232dc3e4ea1b4\\setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' bdist_wheel -d 'C:\Users\ITDforskning\AppData\Local\Temp\pip-wheel-twrpw67c'
       cwd: C:\Users\ITDforskning\AppData\Local\Temp\pip-install-47_87ann\openexr_3db9b944eb864b58bbf232dc3e4ea1b4\
  Complete output (16 lines):
  Looking for libOpenEXR...
  running bdist_wheel
  running build
  running build_py
  creating build
  creating build\lib.win-amd64-3.9
  copying Imath.py -> build\lib.win-amd64-3.9
  running build_ext
  building 'OpenEXR' extension
  creating build\temp.win-amd64-3.9
  creating build\temp.win-amd64-3.9\Release
  C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\VC\Tools\MSVC\14.29.30133\bin\HostX86\x64\cl.exe /c /nologo /Ox /W3 /GL /DNDEBUG /MD -I/usr/include/OpenEXR -I/usr/local/include/OpenEXR -I/opt/local/include/OpenEXR -I/usr/include/Imath -I/usr/local/include/Imath -I/opt/local/include/Imath -IC:\Users\ITDforskning\Anaconda3\envs\Hamid\include -IC:\Users\ITDforskning\Anaconda3\envs\Hamid\include -IC:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\VC\Tools\MSVC\14.29.30133\include -IC:\Program Files (x86)\Windows Kits\NETFXSDK\4.8\include\um -IC:\Program Files (x86)\Windows Kits\10\include\10.0.19041.0\ucrt -IC:\Program Files (x86)\Windows Kits\10\include\10.0.19041.0\shared -IC:\Program Files (x86)\Windows Kits\10\include\10.0.19041.0\um -IC:\Program Files (x86)\Windows Kits\10\include\10.0.19041.0\winrt -IC:\Program Files (x86)\Windows Kits\10\include\10.0.19041.0\cppwinrt /EHsc /TpOpenEXR.cpp /Fobuild\temp.win-amd64-3.9\Release\OpenEXR.obj -g -DVERSION="1.3.9"
  cl : Command line warning D9002 : ignoring unknown option '-g'
  OpenEXR.cpp
  OpenEXR.cpp(36): fatal error C1083: Cannot open include file: 'ImfIO.h': No such file or directory
  error: command 'C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\BuildTools\\VC\\Tools\\MSVC\\14.29.30133\\bin\\HostX86\\x64\\cl.exe' failed with exit code 2
  ----------------------------------------
  ERROR: Failed building wheel for openexr
  Running setup.py clean for openexr
Failed to build openexr
Installing collected packages: openexr
    Running setup.py install for openexr ... error
    ERROR: Command errored out with exit status 1:
     command: 'C:\Users\ITDforskning\Anaconda3\envs\Hamid\python.exe' -u -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'C:\\Users\\ITDforskning\\AppData\\Local\\Temp\\pip-install-47_87ann\\openexr_3db9b944eb864b58bbf232dc3e4ea1b4\\setup.py'"'"'; __file__='"'"'C:\\Users\\ITDforskning\\AppData\\Local\\Temp\\pip-install-47_87ann\\openexr_3db9b944eb864b58bbf232dc3e4ea1b4\\setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' install --record 'C:\Users\ITDforskning\AppData\Local\Temp\pip-record-rxquk8ht\install-record.txt' --single-version-externally-managed --compile --install-headers 'C:\Users\ITDforskning\Anaconda3\envs\Hamid\Include\openexr'
         cwd: C:\Users\ITDforskning\AppData\Local\Temp\pip-install-47_87ann\openexr_3db9b944eb864b58bbf232dc3e4ea1b4\
    Complete output (16 lines):
    Looking for libOpenEXR...
    running install
    running build
    running build_py
    creating build
    creating build\lib.win-amd64-3.9
    copying Imath.py -> build\lib.win-amd64-3.9
    running build_ext
    building 'OpenEXR' extension
    creating build\temp.win-amd64-3.9
    creating build\temp.win-amd64-3.9\Release
    C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\VC\Tools\MSVC\14.29.30133\bin\HostX86\x64\cl.exe /c /nologo /Ox /W3 /GL /DNDEBUG /MD -I/usr/include/OpenEXR -I/usr/local/include/OpenEXR -I/opt/local/include/OpenEXR -I/usr/include/Imath -I/usr/local/include/Imath -I/opt/local/include/Imath -IC:\Users\ITDforskning\Anaconda3\envs\Hamid\include -IC:\Users\ITDforskning\Anaconda3\envs\Hamid\include -IC:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\VC\Tools\MSVC\14.29.30133\include -IC:\Program Files (x86)\Windows Kits\NETFXSDK\4.8\include\um -IC:\Program Files (x86)\Windows Kits\10\include\10.0.19041.0\ucrt -IC:\Program Files (x86)\Windows Kits\10\include\10.0.19041.0\shared -IC:\Program Files (x86)\Windows Kits\10\include\10.0.19041.0\um -IC:\Program Files (x86)\Windows Kits\10\include\10.0.19041.0\winrt -IC:\Program Files (x86)\Windows Kits\10\include\10.0.19041.0\cppwinrt /EHsc /TpOpenEXR.cpp /Fobuild\temp.win-amd64-3.9\Release\OpenEXR.obj -g -DVERSION="1.3.9"
    cl : Command line warning D9002 : ignoring unknown option '-g'
    OpenEXR.cpp
    OpenEXR.cpp(36): fatal error C1083: Cannot open include file: 'ImfIO.h': No such file or directory
    error: command 'C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\BuildTools\\VC\\Tools\\MSVC\\14.29.30133\\bin\\HostX86\\x64\\cl.exe' failed with exit code 2
    ----------------------------------------
ERROR: Command errored out with exit status 1: 'C:\Users\ITDforskning\Anaconda3\envs\Hamid\python.exe' -u -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'C:\\Users\\ITDforskning\\AppData\\Local\\Temp\\pip-install-47_87ann\\openexr_3db9b944eb864b58bbf232dc3e4ea1b4\\setup.py'"'"'; __file__='"'"'C:\\Users\\ITDforskning\\AppData\\Local\\Temp\\pip-install-47_87ann\\openexr_3db9b944eb864b58bbf232dc3e4ea1b4\\setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' install --record 'C:\Users\ITDforskning\AppData\Local\Temp\pip-record-rxquk8ht\install-record.txt' --single-version-externally-managed --compile --install-headers 'C:\Users\ITDforskning\Anaconda3\envs\Hamid\Include\openexr' Check the logs for full command output.

```

#### miniexr

```
python miniexr.py
Traceback (most recent call last):
  File "C:\Users\ITDforskning\Desktop\exr-experiments\miniexr.py", line 4, in <module>
    reader = minexr.load(fp)
  File "C:\Users\ITDforskning\Anaconda3\envs\Hamid\lib\site-packages\minexr\reader.py", line 193, in load
    return MinExrReader(fp)
  File "C:\Users\ITDforskning\Anaconda3\envs\Hamid\lib\site-packages\minexr\reader.py", line 39, in __init__
    self._read_header()
  File "C:\Users\ITDforskning\Anaconda3\envs\Hamid\lib\site-packages\minexr\reader.py", line 112, in _read_header
    assert self.compr == 0x00, 'Compression not supported.'
AssertionError: Compression not supported.
```

#### OpenCV

`python viewer.py` results in empty window
