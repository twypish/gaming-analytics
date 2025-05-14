import React, { useEffect, useState } from 'react';
import {
  AppBar,
  Box,
  CircularProgress,
  Container,
  CssBaseline,
  Grid,
  Paper,
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableRow,
  ThemeProvider,
  Toolbar,
  Typography,
  createTheme
} from '@mui/material';

const theme = createTheme({
  palette: {
    mode: 'light',
    primary: {
      main: '#1976d2'
    },
    background: {
      default: '#f4f4f4'
    }
  }
});

function App() {
  const [games, setGames] = useState([]);
  const [leaders, setLeaders] = useState({});

  useEffect(() => {
    const fetchGames = async () => {
      const res = await fetch('http://localhost:5000/games');
      const data = await res.json();
      setGames(data);
    };
    fetchGames();
  }, []);

  useEffect(() => {
    const fetchLeaders = async () => {
      const newLeaders = {};
      for (const game of games) {
        try {
          const res = await fetch(`http://localhost:5000/leaderboard?game=${game}`);
          const data = await res.json();
          newLeaders[game] = data;
        } catch (err) {
          console.error(`Failed to fetch leaderboard for ${game}`);
        }
      }
      setLeaders(newLeaders);
    };

    fetchLeaders();
    const interval = setInterval(fetchLeaders, 3000);
    return () => clearInterval(interval);
  }, [games]);

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <AppBar position="sticky">
        <Toolbar>
          <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
            Gaming Analytics Dashboard
          </Typography>
        </Toolbar>
      </AppBar>
      <Container sx={{ mt: 4, mb: 4 }}>
        <Typography variant="h4" gutterBottom align="center">
          Real-Time Game Leaderboards
        </Typography>
        <Grid container spacing={4}>
          {games.map((game) => (
            <Grid item xs={12} sm={6} md={4} key={game}>
              <Paper elevation={3} sx={{ padding: 2 }}>
                <Typography variant="h6" align="center" gutterBottom>
                  {game}
                </Typography>
                {leaders[game] ? (
                  <Table size="small">
                    <TableHead>
                      <TableRow>
                        <TableCell>Rank</TableCell>
                        <TableCell>Player</TableCell>
                        <TableCell>Score</TableCell>
                        <TableCell>Kills</TableCell>
                        <TableCell>Assists</TableCell>
                        <TableCell>Objectives</TableCell>
                        <TableCell>Gold</TableCell>
                      </TableRow>
                    </TableHead>
                    <TableBody>
                      {leaders[game].map((player, index) => (
                        <TableRow key={player.player_id}>
                          <TableCell>{index + 1}</TableCell>
                          <TableCell>{player.player_id}</TableCell>
                          <TableCell>{player.score}</TableCell>
                          <TableCell>{player.kill || 0}</TableCell>
                          <TableCell>{player.assist || 0}</TableCell>
                          <TableCell>{player.objective || 0}</TableCell>
                          <TableCell>{player.gold_earned || 0}</TableCell>
                        </TableRow>
                      ))}
                    </TableBody>
                  </Table>
                ) : (
                  <Box textAlign="center" py={2}>
                    <CircularProgress />
                  </Box>
                )}
              </Paper>
            </Grid>
          ))}
        </Grid>
      </Container>
    </ThemeProvider>
  );
}

export default App;
