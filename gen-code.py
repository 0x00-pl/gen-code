import sys

name= sys.argv[1]
code= '''
static int clsld_'''+name+'''( \\
        cha_err_t *err, \\
        io_stream_t *io, \\
        cha_'''+name+'''_t **out)
{
    int ret = 0;
    cha_'''+name+'''_t *new_'''+name+''' = NULL;

    CHA_CLSLD_NEW(goto fail, '''+name+''');

    CHA_CLSLD_READ_CHECK_u2(goto fail, new_'''+name+'''xxxxx, io);
    
    CHA_CLSLD_CALL_CHECK(
      goto fail,
      clsld_attribute_info_xxxxxx(
	err,io,
	&new_'''+name+'''xxxxx,
	new_'''+name+'''xxxxx
      ));

    *out = new_'''+name+''';

    goto done;
fail:
    cha_'''+name+'''_destroy(new_'''+name+''');
done:
    return ret;
}
'''


print (code)
