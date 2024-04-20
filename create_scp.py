import os

trainings = [f'/Users/elijahjohnson/Downloads/proj/output_files/string_{i}/{i}_{j}.wav' if i!=0 else f'/Users/elijahjohnson/Downloads/proj/input_files/0_{j}.wav' for i in range(0,7) for j in range(1,66)] #EDIT Directory HERE
testings = [f'/Users/elijahjohnson/Downloads/proj/output_files/string_{i}/{i}_{j}.wav' if i!=0 else f'/Users/elijahjohnson/Downloads/proj/input_files/0_{j}.wav' for i in range(0,7) for j in range(131,196)] #EDIT Directory HERE
validations = [f'/Users/elijahjohnson/Downloads/proj/output_files/string_{i}/{i}_{j}.wav' if i!=0 else f'/Users/elijahjohnson/Downloads/proj/input_files/0_{j}.wav' for i in range(0,7) for j in range(66,131)] #EDIT Directory HERE
training_scps = [f"tr_{i}.scp" if i!=0 else f"tr_mix.scp" for i in range(0,7)]
test_scps = [f"tt_{i}.scp"  if i!=0 else f"tt_mix.scp" for i in range(0,7)]
validations_scps = [f"cv_{i}.scp"  if i!=0 else f"cv_mix.scp" for i in range(0,7)]

# def scp_convert(scps, nscps):
#     for idx, s in enumerate(scps):
#         f = open(s,'w')
#         for root, dirs, files in os.walk(nscps[idx]):
#             files.sort()
#             for file in files:
#                 print(file+" "+root+'/'+file)
#                 f.write(file+" "+root+'/'+file)
#                 f.write('\n')

def scp_convert(scps, paths):
    for scp, path in zip(scps, paths):
        with open(scp, 'w') as file:
            for p in path:
                file.write(f"{os.path.basename(p)} {p}\n")
                print(f"{os.path.basename(p)} {p}")

training_sets = [[f for f in trainings if f'/{i}_' in f] for i in range(7)]
testing_sets = [[f for f in testings if f'/{i}_' in f] for i in range(7)]
validation_sets = [[f for f in validations if f'/{i}_' in f] for i in range(7)]
    
# scp_convert(training_scps, trainings)
# scp_convert(test_scps, testings)
# scp_convert(validations_scps, validations)
                
scp_convert(training_scps, training_sets)
scp_convert(test_scps, testing_sets)
scp_convert(validations_scps, validation_sets)