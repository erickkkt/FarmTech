import React, { useEffect, useState } from 'react';
import {
  Container,
  Grid,
  Paper,
  Typography,
  Box,
  Card,
  CardContent,
} from '@mui/material';
import {
  Agriculture,
  Pets,
  ShoppingCart,
  Vaccines,
} from '@mui/icons-material';
import { farmService, animalService, productService, vaccinationService } from '../services/dataService';

const Dashboard = () => {
  const [stats, setStats] = useState({
    farms: 0,
    animals: 0,
    products: 0,
    vaccinations: 0,
  });

  useEffect(() => {
    const fetchStats = async () => {
      try {
        const [farms, animals, products, vaccinations] = await Promise.all([
          farmService.getAll(),
          animalService.getAll(),
          productService.getAll(),
          vaccinationService.getAll(),
        ]);

        setStats({
          farms: farms.data.count || farms.data.length || 0,
          animals: animals.data.count || animals.data.length || 0,
          products: products.data.count || products.data.length || 0,
          vaccinations: vaccinations.data.count || vaccinations.data.length || 0,
        });
      } catch (error) {
        console.error('Error fetching stats:', error);
      }
    };

    fetchStats();
  }, []);

  const StatCard = ({ title, value, icon, color }) => (
    <Card>
      <CardContent>
        <Box display="flex" alignItems="center" justifyContent="space-between">
          <Box>
            <Typography color="textSecondary" gutterBottom>
              {title}
            </Typography>
            <Typography variant="h3">{value}</Typography>
          </Box>
          <Box sx={{ color: color, fontSize: 48 }}>
            {icon}
          </Box>
        </Box>
      </CardContent>
    </Card>
  );

  return (
    <Container maxWidth="lg" sx={{ mt: 4, mb: 4 }}>
      <Typography variant="h4" gutterBottom>
        Dashboard
      </Typography>
      
      <Grid container spacing={3}>
        <Grid item xs={12} sm={6} md={3}>
          <StatCard
            title="Total Farms"
            value={stats.farms}
            icon={<Agriculture />}
            color="primary.main"
          />
        </Grid>
        <Grid item xs={12} sm={6} md={3}>
          <StatCard
            title="Total Animals"
            value={stats.animals}
            icon={<Pets />}
            color="success.main"
          />
        </Grid>
        <Grid item xs={12} sm={6} md={3}>
          <StatCard
            title="Marketplace Products"
            value={stats.products}
            icon={<ShoppingCart />}
            color="warning.main"
          />
        </Grid>
        <Grid item xs={12} sm={6} md={3}>
          <StatCard
            title="Vaccinations"
            value={stats.vaccinations}
            icon={<Vaccines />}
            color="error.main"
          />
        </Grid>
      </Grid>

      <Grid container spacing={3} sx={{ mt: 3 }}>
        <Grid item xs={12}>
          <Paper sx={{ p: 3 }}>
            <Typography variant="h6" gutterBottom>
              Welcome to FarmTech Admin Dashboard
            </Typography>
            <Typography variant="body1">
              Manage your farms, animals, vaccinations, and marketplace from this central dashboard.
            </Typography>
          </Paper>
        </Grid>
      </Grid>
    </Container>
  );
};

export default Dashboard;
