pk = lambda x, k: sum((x - x.mean())*(np.roll(x, k)-np.roll(x, k).mean())/(x.std()*np.roll(x, k).std()))/len(x)