import numpy as np


def vecinosMasCercanos(watershed,water_list,cell_idx,paramDist):
    total_area = np.prod(watershed.shape)
    cell_coords = np.mean(np.where(water_list[0]==cell_idx), axis=1)
    size_cell = []
    paramArea = 1.5
    #paramDist = 1.5
    cell_idx_history = [cell_idx]
    ##agregar función
    rows, cols = np.where(water_list[0]==cell_idx)
    borde=(1 in rows or 387 in rows or 1 in cols or 387 in cols)
    unica=(cell_idx in np.unique(water_list[0])) 
    iterator=0
    cont=0
    closestList=[]
    bol=False
    #if (unica==False) or (borde==True):
     #   return print("La célula pertenece a borde o no es única")
    #else:
    for water in water_list[1:]:
        # Get coords of all cells
        new_cords = [np.mean(np.where(water==idx), axis=1) for idx in np.unique(water)[1:]]
        # Find nearest neightbor index
        closest_idx = np.argmin(np.sum((np.stack(new_cords) - cell_coords)**2, axis=1))#si se pierde tamaño NAN agregar condiciones
        closest = np.sum((np.stack(new_cords) - cell_coords)**2, axis=1)
        uno=closest
        cs=sorted(uno)
        distCercana=cs[0]
        closestList.append(distCercana)
        nn_idx = np.unique(water)[1:][closest_idx]
        # Save index and area 
        cell_idx_history.append(nn_idx)
        #comparar el area de la anterior con la nueva/ si es mas pequeño de la mitad o mas grande que el doble
        areaCelulaActual = (100*len(np.where(water == nn_idx)[0])/total_area)
        if(distCercana > paramDist) or (bol==True):
            size_cell.append(np.nan)
            bol=True
        else:
            if (iterator != 0):
                areaCelulaAnterior = size_cell[iterator-1]
                if (areaCelulaActual < areaCelulaAnterior/paramArea) or (areaCelulaActual> areaCelulaAnterior*paramArea):
                    size_cell.append(areaCelulaAnterior)
                else:
                    size_cell.append(areaCelulaActual)
            else:
                size_cell.append(areaCelulaActual) 
        # update cell coords
        iterator=iterator+1
        cell_coords = np.mean(np.where(water==nn_idx), axis=1) 

    return(cell_idx_history, size_cell,closestList)
