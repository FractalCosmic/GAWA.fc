// components/ContributionDashboard.js
import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import styled from 'styled-components';
import { fetchContributions } from '../store/contributionSlice';
import Card from './Card';

const StyledDashboard = styled.div`
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
`;

const ContributionDashboard = () => {
  const dispatch = useDispatch();
  const { currentUser } = useSelector(state => state.user);
  const { contributions, status, error } = useSelector(state => state.contribution);

  useEffect(() => {
    if (currentUser) {
      dispatch(fetchContributions(currentUser.id));
    }
  }, [currentUser, dispatch]);

  if (status === 'loading') return <div>Loading...</div>;
  if (status === 'failed') return <div>Error: {error}</div>;

  return (
    <StyledDashboard>
      <Card>
        <h2>Total Contributions</h2>
        <p>{contributions.length}</p>
      </Card>
      <Card>
        <h2>Total SG Tokens</h2>
        <p>{contributions.reduce((sum, contrib) => sum + contrib.sgTokens, 0)}</p>
      </Card>
      {contributions.map(contrib => (
        <Card key={contrib.id}>
          <h3>{contrib.componentName}</h3>
          <p>Score: {contrib.score}</p>
          <p>SG Tokens: {contrib.sgTokens}</p>
        </Card>
      ))}
    </StyledDashboard>
  );
};

export default ContributionDashboard;
