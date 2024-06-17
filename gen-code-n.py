import sys

name= sys.argv[1]
coden= '''
static int clsld_'''+name+'''( \\
        cha_err_t *err, \\
        io_stream_t *io, \\
        cha_'''+name+'''_t **out, \\
        size_t count)
{
    int ret = 0;
    cha_'''+name+'''_t *new_'''+name+''' = NULL;
    size_t i;

    CHA_CLSLD_NEW_ARR(goto fail, '''+name+''', count);

    for(i = 0; i<count; i++){
      CHA_CLSLD_READ_CHECK_u2(break, new_attribute_info_xxxxxx_xxxxxx, io);
      CHA_CLSLD_READ_CHECK_u2(break, new_attribute_info_xxxxxx_xxxxxx, io);
    }
    if(ret != 0) {goto fail;}

    *out = new_'''+name+''';

    goto done;
fail:
    cha_'''+name+'''_destroy(new_'''+name+''', count);
done:
    return ret;
}
'''


print (coden)
