import os
from os.path import join

from bench import BenchMeasurement, Bench, verify_files

DIR = os.path.dirname(os.path.realpath(__file__))
SRC_FOLDER = os.path.join(DIR, 'bench/fannkuchredux')

# php
SRC_PHP = join(SRC_FOLDER, "fannkuchredux.php-1.php")

# gphp
SRC_GPHP = join(SRC_FOLDER, "fannkuchredux.php-1.graalphp")

# hack
SRC_HACK = join(SRC_FOLDER, "fannkuchredux.php-1.hack")

# jphp
SRC_JPHP = join(SRC_FOLDER, "fannkuchredux.php-1.jphp")

TEST = 'fannkuchredux-1'

verify_files([SRC_PHP, SRC_GPHP, SRC_HACK, SRC_JPHP])


class BenchmarkFannkuch(Bench):

    def run(self):
        prefix = self.get_test_prefix()
        res = []
        res.append(self.run_php8(TEST, prefix, SRC_PHP, ''))
        res.append(self.run_hack(TEST, prefix, SRC_HACK, ''))
        res.append(self.run_php(TEST, prefix, SRC_PHP, ''))
        res.append(self.run_jphp(TEST, prefix, SRC_JPHP, ''))


        res.append(self.run_graalphp(TEST, prefix, SRC_GPHP, ''))
        res.append(self.run_graalphp_native(TEST, prefix, SRC_GPHP, ''))

        self.extract_and_store_data_array(res)

    def _import_data_manually(self):
        pref = '2020-08-04T22:17:40.611217'
        path = 'measurements/' + pref + '-fannkuchredux.php-1.php-php8.txt'

        self.import_data(path,
                         test_name=TEST,
                         prefix=pref,
                         comment='docker, turbo, 4ghz',
                         binary='php8'
                         )

if __name__ == '__main__':
    bm = BenchmarkFannkuch()
    Bench.skip_jphp = False
    bm.run_jphp(TEST, 'test', SRC_JPHP, '')

    pass
