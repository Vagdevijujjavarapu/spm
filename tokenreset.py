from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
def token(rollno,seconds):
    s=Serializer( 'vrhzbvzelcjghgqh',seconds)
    return s.dumps({'user':rollno}).decode('utf-8')
