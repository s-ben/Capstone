import numpy as np


def subtract(newdoc, newdoc2):


    # newdoc_wav_path = newdoc.file 
    # print newdoc_wav_path
    recording_path = os.path.join(settings.MEDIA_ROOT, 'newdoc.file' )

    # recording_path = os.path.join(settings.MEDIA_ROOT, 'GhostsNStuff_mono_4s.wav' )
    
    rate, data = scipy.io.wavfile.read(recording_path)
    u = data.astype(np.float64)
    d = room_simulate.room_sim(u)
    scaled_d = np.int16(d/np.max(np.abs(d)) * 32767)
    
    output_path = os.path.join(settings.MEDIA_ROOT, 'GhostsNStuff_mono_4s_TEST.wav' )
    write(output_path , 44100, scaled_d)

	
    return d
