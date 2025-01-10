import subprocess
import tempfile

from pymol import cmd

def loadr(filename, host=None, *args, **kwargs):
    '''

    DESCRIPTION

        "loadr" load remote file.

        "loadr" will attempt to load a remote file from the given host.
        If the host is not provided, the action will fallback to loading
        the file with the given name from the local drive.

    USAGE

        loadr filename, [host=None [, *args [, **kwargs]]]

        Example:

            PyMOL> loadr path/to/molecule.pdb, user@host

    NOTE

        This command assumes that iteraction with the remote host
        if configured via SSH keys (typically via ~/.ssh/config;
        remote files are copied via SCP).

    ARGUMENTS

        filename = string: file path or URL
        host = host
        *args, **kwargs = additional arguments to the "load" command

    SEE ALSO

        load

        (c) Sergio M. Santos, University of Aveiro, 1st Feb. 2017

    '''

    if host:
        fname = filename.split('/')[-1]
        tmpdir = tempfile.gettempdir()
        scp_source = host + ':' + filename
        scp_target = tmpdir + '/' + fname

        print(f'Trying to load file "{filename}" from host "{host}" ...')

        try:
            ret_code = subprocess.call(['scp', scp_source, scp_target])
        except Exception as exc:
            print(f'Cannot load remote file {scp_source}')
            print(exc)
            raise
        else:
            if ret_code == 0:
                cmd.load(scp_target, *args, **kwargs)
                print(f'Loaded {scp_source}')
            else:
                print(f'Cannot load file "{filename}" from "{host}":'
                      ' No such file or host!')
    else:
        cmd.load(filename, *args, **kwargs)

    return

cmd.extend('loadr', loadr)
