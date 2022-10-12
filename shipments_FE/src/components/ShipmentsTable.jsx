import React, { useMemo, useState, useEffect,useCallback } from 'react';
import MaterialReactTable from 'material-react-table';
import { shipmentsColumns, newData } from './makeData' ;
import {
  Box,
  Button,
  Dialog,
  DialogActions,
  DialogContent,
  DialogTitle,
  IconButton,
  Stack,
  TextField,
  Tooltip,
} from '@mui/material';
import { Delete, Edit } from '@mui/icons-material';

const ShipmentsTable = () => {
  const columns = useMemo(
    () => shipmentsColumns,
    [],
  );
  const [createModalOpen, setCreateModalOpen] = useState(false);
  
  const [tableData, setTableData] = useState([]);
  const [hardRerender, setHardRerender] = useState('')


useEffect(() => {
  //GET REQUEST
  fetch(
    "http://127.0.0.1:8000/api/shipments/")
      .then((res) => res.json())
      .then((json) => {
        setTableData(json)
      })
}, []);


  const handleSaveRow = async ({ exitEditingMode, row, values }) => {
    //if using flat data and simple accessorKeys/ids, you can just do a simple assignment here.
      console.log('values',values)
    tableData[row.index] = values;
    //send/receive api updates here

      let config ={
          method:"PUT",
          headers:{
              "Content-Type":'application/json',
              "Accept":"application/json"
          },
          body:JSON.stringify({
            ...values
          })
      }
    // EDIT REQUEST
    fetch(
      "http://127.0.0.1:8000/api/shipments/" + values.id,config)
        .then((res) => res.json())
        .then((json) => {
          setTableData([...tableData]);
        })


    exitEditingMode(); //required to exit editing mode
  };
  

  const handleDeleteRow = useCallback(
    (row) => {
      if (
        !window.confirm(`Are you sure you want to delete `)
      ) {
        return;
      }

      //send api delete request here, then refetch or update local table data for re-render
        let config ={
          method:"DELETE",
      }
      console.log('test',row.original.id)
      fetch(
         `http://127.0.0.1:8000/api/shipments/${row.original.id}`,config)
          .then((res) => {
              window.location.reload();
          })


      // Delete row
      // tableData.splice(row.index, 1);
      // setTableData([...tableData]);
    },
    [tableData],
  );

  const handleCreateNewRow = (values) => {
    // CREATE DATA
      let config ={
          method:"POST",
          headers:{
              "Content-Type":'application/json',
              "Accept":"application/json"
          },
          body:JSON.stringify({
            ...values
          })
      }

    fetch(
      "http://127.0.0.1:8000/api/shipments/",config)
        .then((res) => {
            tableData.push(values);
            setTableData([...tableData]
            );})
  };

  return (
    <>
    <MaterialReactTable
      columns={columns}
      data={tableData}
      editingMode="modal" //default
      enableEditing
      initialState={{ columnVisibility: { id: false } }}
      onEditingRowSave={handleSaveRow}
      renderRowActions={({ row, table }) => (
        <Box sx={{ display: 'flex', gap: '1rem' }}>
          <Tooltip arrow placement="left" title="Edit">
            <IconButton onClick={() => table.setEditingRow(row)}>
              <Edit />
            </IconButton>
          </Tooltip>
          <Tooltip arrow placement="right" title="Delete">
            <IconButton color="error" onClick={() => handleDeleteRow(row)}>
              <Delete />
            </IconButton>
          </Tooltip>
        </Box>
      )}
      renderTopToolbarCustomActions={() => (
        <Button
          color="secondary"
          onClick={() => setCreateModalOpen(true)}
          variant="contained"
        >
          Create New Account
        </Button>
      )}
    />
    <CreateNewAccountModal
        columns={columns}
        open={createModalOpen}
        onClose={() => setCreateModalOpen(false)}
        onSubmit={handleCreateNewRow}
      />
    </>
  );
};

export const CreateNewAccountModal = ({ open, columns, onClose, onSubmit }) => {
  const [values, setValues] = useState([]);

  const handleSubmit = () => {
    //put your validation logic here
    onSubmit(values);
    onClose();
  };

  return (
    <Dialog open={open}>
      <DialogTitle textAlign="center">Create New Account</DialogTitle>
      <DialogContent>
        <form onSubmit={(e) => e.preventDefault()}>
          <Stack
            sx={{
              width: '100%',
              minWidth: { xs: '300px', sm: '360px', md: '400px' },
              gap: '1.5rem',
            }}
          >
            {columns.map((column) => (

              <TextField
                key={column.accessorKey}
                label={column.header}
                disabled={ ['id','status'].includes(column.accessorKey) ? true : false }
                name={column.accessorKey}
                onChange={(e) =>
                  setValues({ ...values, [e.target.name]: e.target.value })
                }
              />
            ))}
          </Stack>
        </form>
      </DialogContent>
      <DialogActions sx={{ p: '1.25rem' }}>
        <Button onClick={onClose}>Cancel</Button>
        <Button color="secondary" onClick={handleSubmit} variant="contained">
          Create New Account
        </Button>
      </DialogActions>
    </Dialog>
  );
};
export default ShipmentsTable;