import * as React from 'react';
import { createStyles, makeStyles, Theme } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';
import IconButton from '@material-ui/core/IconButton';
import ListIcon from '@material-ui/icons/List';

import {Link} from 'react-router-dom';

const useStyles = makeStyles(theme =>
  createStyles({
    root: {
      flexGrow: 1,
    },
    menuButton: {
      marginRight: theme.spacing(2),
    },
    title: {
      flexGrow: 1,
    },
  }),
);

function NavHeader(props) {
    const classes = useStyles();
    const { user, authenticated } = props;

    if (user === undefined && authenticated === false) {
        return (
            <AppBar position="static">
                <Toolbar>
                    <IconButton edge="start" className={classes.menuButton} color="inherit" aria-label="menu">
                    <ListIcon />
                    </IconButton>
                    <Typography variant="h6" className={classes.title}>
                        Stuff
                    </Typography>
                    <Link to='/login'>
                        <Button color="inherit">Login</Button>
                    </Link>
                </Toolbar>
            </AppBar>
        )
    }
    return (
        <AppBar position="static">
        <Toolbar>
            <IconButton edge="start" className={classes.menuButton} color="inherit" aria-label="menu">
            <ListIcon />
            </IconButton>
            <Typography variant="h6" className={classes.title}>
                {user}
            </Typography>
            <Button color="inherit">Logout</Button>
        </Toolbar>
    </AppBar>
    )

}

export default NavHeader;
