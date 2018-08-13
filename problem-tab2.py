#                     train on batch
                    if (index + 1) * batch_size > x.shape[0]:
                        epoch = epoch +1
                        print('\nEpoch ' + str(epoch+1) + '/' +  str(epochs))
                        batch = random_x[index * batch_size::]					
                        random_x = x.copy()                        
    						np.random.shuffle(random_x)						
    						index = 0