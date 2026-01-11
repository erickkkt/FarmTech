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
  Vaccines,
  Notifications,
} from '@mui/icons-material';
import { farmService, animalService, vaccinationService, notificationService } from '../services/dataService';

const Dashboard = () => {
  const [stats, setStats] = useState({
    farms: 0,
    animals: 0,
    vaccinations: 0,
    notifications: 0,
  });

  useEffect(() => {
    const fetchStats = async () => {
      try {
        const [farms, animals, vaccinations, notifications] = await Promise.all([
          farmService.getAll(),
          animalService.getAll(),
          vaccinationService.getAll(),
          notificationService.getAll(),
        ]);

        setStats({
          farms: farms.data.count || farms.data.length || 0,
          animals: animals.data.count || animals.data.length || 0,
          vaccinations: vaccinations.data.count || vaccinations.data.length || 0,
          notifications: notifications.data.count || notifications.data.length || 0,
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
        My Dashboard
      </Typography>
      
      <Grid container spacing={3}>
        <Grid item xs={12} sm={6} md={3}>
          <StatCard
            title="My Farms"
            value={stats.farms}
            icon={<Agriculture />}
            color="primary.main"
          />
        </Grid>
        <Grid item xs={12} sm={6} md={3}>
          <StatCard
            title="My Animals"
            value={stats.animals}
            icon={<Pets />}
            color="success.main"
          />
        </Grid>
        <Grid item xs={12} sm={6} md={3}>
          <StatCard
            title="Vaccinations"
            value={stats.vaccinations}
            icon={<Vaccines />}
            color="warning.main"
          />
        </Grid>
        <Grid item xs={12} sm={6} md={3}>
          <StatCard
            title="Notifications"
            value={stats.notifications}
            icon={<Notifications />}
            color="error.main"
          />
        </Grid>
      </Grid>

      <Grid container spacing={3} sx={{ mt: 3 }}>
        <Grid item xs={12}>
          <Paper sx={{ p: 3 }}>
            <Typography variant="h6" gutterBottom>
              Welcome to FarmTech
            </Typography>
            <Typography variant="body1">
              Manage your farms, track your animals, schedule vaccinations, and browse the marketplace all in one place.
            </Typography>
          </Paper>
        </Grid>
      </Grid>
    </Container>
  );
};

export default Dashboard;
