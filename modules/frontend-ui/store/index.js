// store/index.js
import { configureStore } from '@reduxjs/toolkit';
import userReducer from './userSlice';
import contributionReducer from './contributionSlice';

export const store = configureStore({
  reducer: {
    user: userReducer,
    contribution: contributionReducer,
  },
});

// store/userSlice.js
import { createSlice } from '@reduxjs/toolkit';

const userSlice = createSlice({
  name: 'user',
  initialState: {
    currentUser: null,
  },
  reducers: {
    setUser: (state, action) => {
      state.currentUser = action.payload;
    },
    clearUser: (state) => {
      state.currentUser = null;
    },
  },
});

export const { setUser, clearUser } = userSlice.actions;
export default userSlice.reducer;

// store/contributionSlice.js
import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import api from '../api';

export const fetchContributions = createAsyncThunk(
  'contribution/fetchContributions',
  async (userId) => {
    const response = await api.get(`/contributions/${userId}`);
    return response.data;
  }
);

const contributionSlice = createSlice({
  name: 'contribution',
  initialState: {
    contributions: [],
    status: 'idle',
    error: null,
  },
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(fetchContributions.pending, (state) => {
        state.status = 'loading';
      })
      .addCase(fetchContributions.fulfilled, (state, action) => {
        state.status = 'succeeded';
        state.contributions = action.payload;
      })
      .addCase(fetchContributions.rejected, (state, action) => {
        state.status = 'failed';
        state.error = action.error.message;
      });
  },
});

export default contributionSlice.reducer;
