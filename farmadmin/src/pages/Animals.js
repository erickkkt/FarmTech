import React, { useEffect, useState } from 'react';
import {
  Container,
  Typography,
  Button,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Paper,
  IconButton,
  Box,
} from '@mui/material';
import { Edit, Delete, Add } from '@mui/icons-material';
import { animalService } from '../services/dataService';

const Animals = () => {
  const [animals, setAnimals] = useState([]);

  useEffect(() => {
    fetchAnimals();
  }, []);

  const fetchAnimals = async () => {
    try {
      const response = await animalService.getAll();
      setAnimals(response.data.results || response.data);
    } catch (error) {
      console.error('Error fetching animals:', error);
    }
  };

  const handleDelete = async (id) => {
    if (window.confirm('Are you sure you want to delete this animal?')) {
      try {
        await animalService.delete(id);
        fetchAnimals();
      } catch (error) {
        console.error('Error deleting animal:', error);
      }
    }
  };

  return (
    <Container maxWidth="lg" sx={{ mt: 4, mb: 4 }}>
      <Box display="flex" justifyContent="space-between" alignItems="center" mb={3}>
        <Typography variant="h4">Animals</Typography>
        <Button variant="contained" startIcon={<Add />}>
          Add Animal
        </Button>
      </Box>

      <TableContainer component={Paper}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>Tag Number</TableCell>
              <TableCell>Name</TableCell>
              <TableCell>Type</TableCell>
              <TableCell>Breed</TableCell>
              <TableCell>Farm</TableCell>
              <TableCell>Health Status</TableCell>
              <TableCell>Actions</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {animals.map((animal) => (
              <TableRow key={animal.id}>
                <TableCell>{animal.tag_number}</TableCell>
                <TableCell>{animal.name || '-'}</TableCell>
                <TableCell>{animal.animal_type_display}</TableCell>
                <TableCell>{animal.breed}</TableCell>
                <TableCell>{animal.farm_name}</TableCell>
                <TableCell>{animal.health_status}</TableCell>
                <TableCell>
                  <IconButton color="primary" size="small">
                    <Edit />
                  </IconButton>
                  <IconButton
                    color="error"
                    size="small"
                    onClick={() => handleDelete(animal.id)}
                  >
                    <Delete />
                  </IconButton>
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </Container>
  );
};

export default Animals;
