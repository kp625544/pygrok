try:
    import regex as re
except ImportError as e:
    # If you import re, grok_match can't handle regular expression containing atomic group(?>)
    import re
import os

DEFAULT_PATTERNS_DIRS = [os.path.dirname(os.path.abspath(__file__)) + '/pygrok/patterns']

def _reload_patterns(patterns_dirs):
    """
    """
    all_patterns = {}
    for dir in patterns_dirs:
        for f in os.listdir(dir):
            patterns = _load_patterns_from_file(os.path.join(dir, f))
            all_patterns.update(patterns)

    return all_patterns

def _load_patterns_from_file(file):
    """
    """
    patterns = {}
    #print(file)
    with open(file, 'r') as f:
        for l in f:
            l = l.strip()
            #print(type(l))
            if l == '' or l.startswith('#'):
                continue

            #print(l)
            sep = l.find(' ')
            #print(sep)
            pat_name = l[:sep]
            #print(pat_name)
            #print(l[sep:])
            regex_str = l[sep:].strip()
            #print(type(regex_str))
            #pat = Pattern(pat_name, regex_str)
            patterns[pat_name] = regex_str
    return patterns


abcd = _reload_patterns(DEFAULT_PATTERNS_DIRS)
print(abcd['CISCO_ACTION'])
