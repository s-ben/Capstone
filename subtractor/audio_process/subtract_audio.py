import numpy as np
import os
from django.conf import settings

# from django.http import HttpResponse
# from django.shortcuts import render

    
 # -*- coding: utf-8 -*-
# from django.shortcuts import render_to_response
# from django.template import RequestContext
# from django.http import HttpResponseRedirect
# from django.core.urlresolvers import reverse

from django.conf import settings
import os


from .models import Document, User, Audio
# from .forms import DocumentForm


import scipy.io.wavfile
from scipy.io.wavfile import write
import numpy as np
import room_simulate

from django_rq import job

# @job
def subtract(newdoc, newdoc2):


    # newdoc_wav_path = newdoc.file 
    # print newdoc_wav_path


    # recording_path = os.path.join(settings.MEDIA_ROOT, newdoc.file )
    # print newdoc.file
    # type newdoc.file
    # print newdoc.file.url 

    newdoc_filename = os.path.basename(newdoc.file.url)

    # newdoc_url = newdoc.file.url 
    # print type(newdoc_url)

    recording_path = os.path.join(settings.MEDIA_ROOT, newdoc_filename)
    # recording_path = os.path.join(settings.BASE_DIR, newdoc_url)
    # print recording_path
    # print settings.BASE_DIR

    rate, data = scipy.io.wavfile.read(recording_path)
    u = data.astype(np.float64)
    d = room_simulate.room_sim(u)
    scaled_d = np.int16(d/np.max(np.abs(d)) * 32767)
    
    # output_path = os.path.join(settings.MEDIA_ROOT, newdoc_filename+'TEST2.wav' )
    output_filename = os.path.splitext(os.path.basename(newdoc.file.url))[0]
    print output_filename

    output_path = os.path.join(settings.MEDIA_ROOT,output_filename+'_CLEANED.wav')


    # output_path = os.path.join(settings.MEDIA_ROOT, ['/Ghosts_TEST2.wav'] )
    write(output_path , 44100, scaled_d)

	
    return d
