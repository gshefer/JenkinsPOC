import os
print 'This is just a test that checks the environment variables.'
print '\n'.join('{} = {}'.format(k ,v) for k, v in os.environ.items())