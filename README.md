# spyder_tab_issue
When trying to shift-tab the first line in spyder, it deletes most of the text
In this example, when using shift-tab on the first line, the entire first line gets deleted

    						index += 1						
                        self.batch = batch						 

When doing shift-tab on line 7 "np.random.shuffle(random_x)", a bunch of the text gets deleted.
#                     train on batch
                    if (index + 1) * batch_size > x.shape[0]:
                        epoch = epoch +1
                        print('\nEpoch ' + str(epoch+1) + '/' +  str(epochs))
                        batch = random_x[index * batch_size::]					
                        random_x = x.copy()                        
    						np.random.shuffle(random_x)						
    						index = 0
