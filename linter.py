from SublimeLinter.lint import Linter  # or NodeLinter, PythonLinter, ComposerLinter, RubyLinter


class __class__(Linter):
    cmd = 'npx solhint -f visualstudio ${file}'
    tempfile_suffix = "-"
    regex = (
        r'^.+?\((?P<line>\d+),(?P<col>\d+)\): '
        r'(.?(?P<warning>warning)|(?P<error>error)).+?'
        r':(?P<message>.+)'
    )
    multiline = True
    name = 'solhint'
    defaults = {
        'selector': 'source.solidity'
    }
