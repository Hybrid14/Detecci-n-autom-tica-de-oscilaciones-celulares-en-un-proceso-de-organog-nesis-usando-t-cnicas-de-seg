import numpy as np


def vecinosMasCercanos(watershed,water_list,cell_idx):
    total_area = np.prod(watershed.shape)
    cell_coords = np.mean(np.where(water_list[0]==cell_idx), axis=1)
    size_cell = []
    cell_idx_history = [cell_idx]
    ##agregar función
    rows, cols = np.where(water_list[0]==cell_idx)
    borde=(1 in rows or 387 in rows or 1 in cols or 387 in cols)
    unica=(cell_idx in np.unique(water_list[0])) 
    iterator=0
    if (unica==False) or (borde==True):
        return print("La célula pertenece a borde o no es única")
    else:
        for water in water_list[1:]:
            # Get coords of all cells
            new_cords = [np.mean(np.where(water==idx), axis=1) for idx in np.unique(water)[1:]]
            # Find nearest neightbor index
            closest_idx = np.argmin(np.sum((np.stack(new_cords) - cell_coords)**2, axis=1))
            nn_idx = np.unique(water)[1:][closest_idx]
            # Save index and area 
            cell_idx_history.append(nn_idx)
            #comparar el area de la anterior con la nueva/ si es mas pequeño de la mitad o mas grande que el doble
            areaCelulaActual = (100*len(np.where(water == nn_idx)[0])/total_area)
            if (iterator != 0):
                areaCelulaAnterior = size_cell[iterator-1]
                if (areaCelulaActual < areaCelulaAnterior/1.5) or (areaCelulaActual> areaCelulaAnterior*1.5):
                    #size_cell.append(np.nan)
                    size_cell.append(areaCelulaAnterior)
                    #cell_coords = np.mean(np.where(water==cell_idx_history[iterator-1]), axis=1) 
                else:
                    size_cell.append(areaCelulaActual)
                    #cell_coords = np.mean(np.where(water==nn_idx), axis=1) 
            else:
                size_cell.append(areaCelulaActual)
                #cell_coords = np.mean(np.where(water==nn_idx), axis=1) 
            # update cell coords
            iterator=iterator+1
            cell_coords = np.mean(np.where(water==nn_idx), axis=1) 

        return(cell_idx_history, size_cell)
