import wave
import struct

CHUNK_SIZE = 48000 #very big so it doesn't create a million files for testing rn, but probably should be much smaller

def slice_input_wav(input_filename, starting_idx, chunk_size=CHUNK_SIZE):
    # Open the input WAV file
    with wave.open(input_filename, 'rb') as infile:
        # Get WAV file parameters
        num_channels = infile.getnchannels()
        sample_width = infile.getsampwidth()
        frame_rate = infile.getframerate()
        num_frames = infile.getnframes()

        # Calculate the total number of chunks
        total_chunks = (num_frames + chunk_size - 1) // chunk_size

        # Read the frames
        frames = infile.readframes(num_frames)
        sample_format = f'>{num_channels}h' if sample_width == 2 else f'>{num_channels}b'

        # Convert frames to samples
        #samples = struct.unpack_from(sample_format * num_frames, frames)
        samples = struct.unpack_from(f'<{num_frames}h', frames)

        # Iterate through each chunk
        for chunk_index in range(total_chunks):
            # Calculate the start and end index of the current chunk
            start_index = chunk_index * chunk_size
            end_index = min(start_index + chunk_size, num_frames)

            # Get the samples for the current chunk
            chunk_samples = samples[start_index:end_index]

            # Create a new file name for the chunk
            output_filename = f'0_{starting_idx + chunk_index + 1}.wav'

            # Open a new WAV file for the chunk
            with wave.open("input_files/" + output_filename, 'wb') as outfile:
                # Set WAV file parameters (same as input file)
                outfile.setnchannels(num_channels)
                outfile.setsampwidth(sample_width)
                outfile.setframerate(frame_rate)

                # Convert the samples to binary data
                binary_data = struct.pack(f'<{len(chunk_samples)}h', *chunk_samples)

                # Write the binary data to the new WAV file
                outfile.writeframes(binary_data)

            #print(f'Saved chunk {starting_idx + chunk_index + 1} as {output_filename}')

def slice_output_wav(input_filename, str_num, starting_idx, chunk_size=CHUNK_SIZE):
    # Open the input WAV file
    with wave.open(input_filename, 'rb') as infile:
        # Get WAV file parameters
        num_channels = infile.getnchannels()
        sample_width = infile.getsampwidth()
        frame_rate = infile.getframerate()
        num_frames = infile.getnframes()

        # Calculate the total number of chunks
        total_chunks = (num_frames + chunk_size - 1) // chunk_size

        # Read the frames
        frames = infile.readframes(num_frames)
        #sample_format = f'>{num_channels}h' if sample_width == 2 else f'>{num_channels}b'

        # Convert frames to samples
        #samples = struct.unpack_from(sample_format * num_frames, frames)
        samples = struct.unpack_from(f'<{num_frames}h', frames)

        # Iterate through each chunk
        for chunk_index in range(total_chunks):
            # Calculate the start and end index of the current chunk
            start_index = chunk_index * chunk_size
            end_index = min(start_index + chunk_size, num_frames)

            # Get the samples for the current chunk
            chunk_samples = samples[start_index:end_index]

            # Create a new file name for the chunk
            output_filename = f'{str_num}_{starting_idx + chunk_index + 1}.wav'

            # Open a new WAV file for the chunk
            with wave.open(f"output_files/string_{str_num}/" + output_filename, 'wb') as outfile:
                # Set WAV file parameters (same as input file)
                outfile.setnchannels(num_channels)
                outfile.setsampwidth(sample_width)
                outfile.setframerate(frame_rate)

                # Convert the samples to binary data
                binary_data = struct.pack(f'<{len(chunk_samples)}h', *chunk_samples)

                # Write the binary data to the new WAV file
                outfile.writeframes(binary_data)

            print(f'Saved chunk {starting_idx + chunk_index + 1} as {output_filename}')

# Example usage
# slice input wave takes in the total audio and cuts it into chunks according to CHUNK_SIZE, writing
# the chunks to the input_files folder. slice output wave does the same thing for each string and 
# puts the chunk files in the corresponding folders. The 0 in in all the function calls below
# is for a global counter, so we can run this one one song, figure out the total chunks,
# and replace the 0 with that last chunk number so our dataset is continuous and not based on
# songs.

slice_input_wav('full_wavs/total_audio_1.wav', 0)
slice_output_wav('full_wavs/bottom_e_audio_1.wav',1, 0)
slice_output_wav('full_wavs/a_audio_1.wav',2, 0)
slice_output_wav('full_wavs/d_audio_1.wav',3, 0)
slice_output_wav('full_wavs/g_audio_1.wav',4, 0)
slice_output_wav('full_wavs/b_audio_1.wav',5, 0)
slice_output_wav('full_wavs/top_e_audio_1.wav',6, 0)
