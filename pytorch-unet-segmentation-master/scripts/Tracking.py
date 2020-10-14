import numpy as np


def vecinosMasCercanos(watershed,water_list,cell_idx):
    total_area = np.prod(watershed.shape)
    cell_coords = np.mean(np.where(water_list[0]==cell_idx), axis=1)
    size_cell = []
    cell_idx_history = [cell_idx]

    for water in water_list[1:]:
        # Get coords of all cells
        new_cords = [np.mean(np.where(water==idx), axis=1) for idx in np.unique(water)[1:]]
        # Find nearest neightbor index
        closest_idx = np.argmin(np.sum((np.stack(new_cords) - cell_coords)**2, axis=1))
        nn_idx = np.unique(water)[1:][closest_idx]
        # Save index and area, agregar condiciones 
        cell_idx_history.append(nn_idx)
        size_cell.append(100*len(np.where(water == nn_idx)[0])/total_area)
        # update cell coords
        cell_coords = np.mean(np.where(water==nn_idx), axis=1)

    #elimino los mayores a 3
    new_size_cell=[]
    for size in size_cell:
        if (size<3):
            new_size_cell.append(size)
            
    return(cell_idx_history, new_size_cell)
